# Step 1: Install dependencies in the build stage
FROM node:18 AS build

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose the port that Vite uses by default
EXPOSE 5173

# Step 2: Run Vite dev server for development mode
CMD ["npm", "run", "dev"]