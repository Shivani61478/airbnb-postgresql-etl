from extract import extract
from transform import transform
from load import load

df = extract()

print(df.head())
print(f"Rows extracted: {len(df)}")

cleaned_data = transform(df)


print(cleaned_data.head())
print(f"Rows after cleaning: {len(cleaned_data)}")

load(cleaned_data)

