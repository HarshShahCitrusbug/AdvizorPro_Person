import json
from core.models import Brokers
from django.core import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            queryset = Brokers.objects.all()
            total_count = queryset.count()
            # Determine the size of each chunk
            chunk_size = total_count // 4

            # Divide the queryset into four parts
            chunks = [queryset[i * chunk_size : (i + 1) * chunk_size] for i in range(4)]

            # Handle the remainder if total_count is not perfectly divisible by 4
            if total_count % 4 != 0:
                chunks[-1] |= queryset[4 * chunk_size :]

            # Iterate over the chunks and serialize each to JSON
            for idx, chunk in enumerate(chunks):
                json_data = serializers.serialize("json", chunk)
                data = json.loads(json_data)

                # Define the file path for each JSON file
                file_path = f"data_{idx + 1}.json"

                # Write JSON data to file
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

            self.stdout.write(self.style.SUCCESS("Successfully created 4 JSON files"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
