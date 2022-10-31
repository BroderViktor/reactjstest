
import requests
# SOAP request URL
url = "https://www.altinn.no/ServiceEngineExternal/ServiceMetaDataExternal.svc"
  
# structured XML
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <soap:Body>
                    <GetAvailableServicesV2>

                    </GetAvailableServicesV2>
                </soap:Body>
            </soap:Envelope>"""
# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# POST request
response = requests.request("GET", url, headers=headers, data=payload)
  
# prints the response
print(response.text)
print(response)