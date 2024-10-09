import json

def are_anagrams(string1, string2):
    clnd_strg1 = ''.join(sorted(string1.replace(" ", "").lower()))
    clnd_strg2 = ''.join(sorted(string2.replace(" ", "").lower()))
    return clnd_strg1 == clnd_strg2

def lambda_handler(event, _):
    body = json.loads(event.get('body', '{}'))
    
    org_strg1 = body.get('string1')
    org_strg2 = body.get('string2')
    
    if not org_strg1 or not org_strg2:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Both string1 and string2 must be provided and non-empty.',
                'eventReceived': event
            })
        }
    
    result = are_anagrams(org_strg1, org_strg2)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'areAnagrams': result,
            'message': f"'{org_strg1}' and '{org_strg2}' are anagrams?: {result}"
        })
    }
