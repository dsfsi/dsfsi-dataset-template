# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Africa/Johannesburg

RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3.8-dev python3.8-venv python3-pip python3-wheel build-essential && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
RUN python3.8 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# install requirements
COPY req.txt .
RUN pip3 install --no-cache-dir -r req.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3-venv && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder-image /opt/venv /opt/venv

COPY . app

# activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

RUN python3 main.py