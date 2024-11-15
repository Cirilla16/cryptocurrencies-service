### FR and QR
- FR 1: View CryptoCurrencies
    - FR 1.1 See all available currencies symbols(digital and physical)
- FR 1.2 See the currency exchange rate
- FR 2: View the historical time series for a digital currency traded on a specific market
    - FR 2.1: VIew daily time series
    - FR 2.2: View weekly time series
    - FR 2.3: View monthly time series

- QR1 Performance
    - QR1.1 Response time. all the interactions between users and the system must be completed within 3 seconds.
        - Why: this service doesn't need too many resources, users want instant feedback
- QR2 Usability
    - QR2.1 Users can choose time intervals and time span for the historical time series
        - Why: users want to see the historical data in different time intervals
    - QR 2.2 Show the historical data in graphic formats
        - Why: users want to see the historical data in a more intuitive way
- QR3 Availability
    - QR3.1 No down time. If the service fails, the system must provide normal service as usual
- QR4 Security
    - QR4.1  Only authorized users can access the information.

### Docker deployment:
- docker build -t cryptocurrencies_service:latest -f Dockerfile .
- docker tag cryptocurrencies_service cirilla16/cryptocurrencies_service:latest
- docker push cirilla16/cryptocurrencies_service:latest
- docker run -itd -p 8000:8000 --env ENV=dev --name cryptocurrencies_service cirilla16/cryptocurrencies_service





 
 
 