FROM python:3.9 as backend

# COPY backend/ frontend/ into the image
WORKDIR /app
COPY ./backend ./backend
COPY ./frontend ./frontend

# Move to backend to install python requirements
WORKDIR /app/backend
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y npm

# Move to frontend to install js requirements (npm)
WORKDIR /app/frontend
RUN npm install

# Move back to app/
WORKDIR /app
EXPOSE 8080
EXPOSE 5000

# Copy the script into the image
COPY ./script.sh ./script.sh
CMD ["bash", "./script.sh"]