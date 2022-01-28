#!/usr/bin/env python3

import os
import boto3

#Explicit Client configuration
AWS_ACCESS_KEY = os.environ['aws_access_key_id']
AWS_SECRET_KEY = os.environ['aws_secret_access_key']

polly = boto3.client('polly',
	region_name='us-west-1',
	aws_access_key_id=AWS_ACCESS_KEY,
	aws_secret_access_key=AWS_SECRET_KEY)

result = polly.synthesize_speech(Text='Hello World!',
		OutputFormat='mp3',
		VoiceId='Aditi')

# Save the audio from the response
audio = result['AudioStream'].read()
with open('helloworld.mp3', "wb") as file:
	file.write(audio)
		
