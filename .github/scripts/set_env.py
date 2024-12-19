import sys
import os

def set_env_vars(environment):
    if environment == 'qa':
        app_service_name = os.getenv('AZURE_QA_APP_SERVICE_NAME')
        publish_profile = os.getenv('AZURE_QA_PUBLISH_PROFILE')
    elif environment == 'prod':
        app_service_name = os.getenv('AZURE_PROD_APP_SERVICE_NAME')
        publish_profile = os.getenv('AZURE_PROD_PUBLISH_PROFILE')
    else:
        raise ValueError(f"Unknown environment: {environment}")

    # Save the environment variables to GitHub outputs
    print(f"::set-output name=app_service_name::{app_service_name}")
    print(f"::set-output name=publish_profile::{publish_profile}")

if __name__ == "__main__":
    environment = sys.argv[1]
    set_env_vars(environment)
