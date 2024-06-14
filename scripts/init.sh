#!/bin/bash

file="data/dvf.csv"
temp_file=$(mktemp)
endpoint="https://dvf-api.data.gouv.fr/dvf/csv/?dep=31"

curl "https://dvf-api.data.gouv.fr/dvf/csv/?dep=31" --output "$file"

header=$(head -n 1 "$file")

echo "$header" >> "$temp_file"

while IFS= read -r line; do
  # If the line is not equal to the header, print it to the temporary file
  if [[ "$line" != "$header" ]]; then
    echo "$line" >> "$temp_file"
  fi
done < "$file"

mv "$temp_file" "$file"
