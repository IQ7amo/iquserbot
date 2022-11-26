FROM IQerenn/iquserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/IQerenn/iquserbot /root/IQBOT
#working directory 
WORKDIR /root/iquserbot
RUN apk add --update --no-cache p7zip
# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/iquserbot/bin:$PATH"

CMD ["python3","-m","iquserbot"]
