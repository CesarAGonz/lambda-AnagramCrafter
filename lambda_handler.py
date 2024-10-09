import json

def are_anagrams(string1, string2):
    string1 = ''.join(sorted(string1.replace(" ", "").lower()))
    string2 = ''.join(sorted(string2.replace(" ", "").lower()))
    return string1 == string2

def lambda_handler(event, context):
    string1 = event.get('string1', '')
    string2 = event.get('string2', '')

    result = are_anagrams(string1, string2)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'areAnagrams': result,
            'message': f"'{string1}' and '{string2}' are anagrams?: {result}"
        })
    }
