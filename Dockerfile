FROM IQerenn/IQBOT:slim-buster

#clonning repo 
RUN git clone https://github.com/IQerenn/IQBOT /root/IQBOT
#working directory 
WORKDIR /root/IQBOT
RUN apk add --update --no-cache p7zip
# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/IQBOT/bin:$PATH"

CMD ["python3","-m","IQBOT"]
