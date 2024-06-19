from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["openai_apikey"])

assistant = client.beta.assistants.create(
    name="Broker data analyst",
    instructions="You are an expert data analyst. Use you knowledge base to answer questions and provide asked details about the brokers.",
    model="gpt-4-turbo",
    tools=[{"type": "file_search"}],
)


# Create a vector store caled "Financial Statements"
vector_store = client.beta.vector_stores.create(name="Financial Statements")

# Ready the files for upload to OpenAI
file_paths = [
    "core/data_1.json",
    "core/data_2.json",
    "core/data_3.json",
    "core/data_4.json",
]
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

# You can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

print("assistant_id: ", assistant.id)
print("vector_store_id: ", vector_store.id)
print("file_batch_id: ", file_batch.id)
