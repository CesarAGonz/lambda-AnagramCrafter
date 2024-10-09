import json

def are_anagrams(string1, string2):
    clnd_strg1 = ''.join(sorted(string1.replace(" ", "").lower()))
    clnd_strg2 = ''.join(sorted(string2.replace(" ", "").lower()))
    return clnd_strg1 == clnd_strg2

def lambda_handler(event, context):
    org_strg1 = event.get('string1', '')
    org_strg2 = event.get('string2', '')
    
    result = are_anagrams(org_strg1, org_strg2)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'areAnagrams': result,
            'message': f"'{org_strg1}' and '{org_strg2}' are anagrams?: {result}"
        })
    }
