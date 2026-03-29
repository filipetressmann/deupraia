wget -O response.json \
  --compression=auto \
  --method=POST \
  --header="Content-Type: application/json" \
  --header="Origin: https://app.powerbi.com" \
  --header="Referer: https://app.powerbi.com/" \
  --header="User-Agent: Mozilla/5.0" \
  --header="ActivityId: 857fd611-c8a3-b557-185c-1c6f6e7140c3" \
  --header="RequestId: f4638c58-b7dd-84e0-a50d-6cc797be7fc7" \
  --header="X-PowerBI-ResourceKey: e2d2d188-74bb-484b-b36f-b34de373b210" \
  --body-file=./payloads/es/vila-velha/payload.json \
  "https://wabi-brazil-south-b-primary-api.analysis.windows.net/public/reports/querydata"