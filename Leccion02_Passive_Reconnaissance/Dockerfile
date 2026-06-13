# 1. Specify the base image
FROM node:24-alpine

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependency files first to utilize Docker caching
COPY package*.json ./

# 4. Install production dependencies
RUN npm install --omit=dev

# 5. Copy the remaining application source code
COPY . .

# 6. Expose the port the app listens on
EXPOSE 3000
