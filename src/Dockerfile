FROM python:3.8-alpine

RUN mkdir /app/
WORKDIR /app/

ENV URL "https://api.coinbase.com/v2/prices/spot?currency="
ENV ACCEPTED_CURRENCIES ["EUR", "GBP", "USD","JPY"]

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt    

COPY ./coinbase_requests.py /app/
ENTRYPOINT [ "python" ]
CMD ["coinbase_requests.py" ]
EXPOSE 5001