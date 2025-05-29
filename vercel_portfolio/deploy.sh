#!/bin/bash

# Install dependencies
npm install

# Build the project
npm run build

# Deploy to Vercel
vercel --prod
