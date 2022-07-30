# Tulip Dashboard Data Pump

## Problem
We start with an empty bucket that will serve data to the Tulip dashboard. We need to fill that bucket with data - hydrate it. We have pipelines that can feed on-chain data from Growth Vector. 

## Solution
The Tulip Dashboard Data Pump is a service that pulls data from an API and then deposits it into a bucket in a meaningful package. The data may or may not be ready to be displayed by the dashboard once deposited by the data pump. The Tulip Dashboard Data Pump aims to only pull data from pipelines and deposit it into buckets. Any significant transformation of the pipeline data should be done downstream of the Data Pump.

## Implementation Overview

The Tulip Dashboard Data Pump is implemented as a Cloud Run Job. Therefore, we develop our pump logic, package it into a container and then deploy it into Cloud Run.

Since the Data Pump does not need to run continuously, we will also use Google Cloud Scheduler to schedule the Cloud Run Job.

## Path of Least Resistance

This simple job can be coded into many different languages. I am most comfortable with Python so we'll develop the first version in that language.