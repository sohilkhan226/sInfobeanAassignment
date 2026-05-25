# Q143: Check if a string is valid JSON format (basic check).
# Input: S = '{"key": "value"}'
# Output: True
import json
S = '{"key": "value"}'
try:
    json.loads(S)
    print(True)
except:
    print(False)