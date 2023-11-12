import boto3


def upload_to_s3():
    """
    Upload file to S3.
    """
    try:
        s3 = boto3.resource(
            service_name="s3",
            region_name="sa-east-1",
        )

        s3.meta.client.upload_file(
            "./files/addresses.csv", "techtestsbancol", "addresses.csv"
        )

    except Exception as e:
        print(f"Error en la carga desde s3: {str(e)}")


def run():
    upload_to_s3()


if __name__ == "__main__":
    run()
