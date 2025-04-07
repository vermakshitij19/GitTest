import boto3

def lambda_handler(event, context):
    try:
        rds = boto3.client('rds', region_name='ap-south-1')

        db_instance_id = 'your-db-instance-identifier'  # Change this to your DB instance ID

        # Optional: if you want to keep a final snapshot, set this to True and give it a name
        skip_final_snapshot = True
        final_snapshot_id = 'final-snapshot-before-delete'  # Only needed if skip_final_snapshot=False

        if skip_final_snapshot:
            response = rds.delete_db_instance(
                DBInstanceIdentifier=db_instance_id,
                SkipFinalSnapshot=True
            )
        else:
            response = rds.delete_db_instance(
                DBInstanceIdentifier=db_instance_id,
                SkipFinalSnapshot=Tru,
                FinalDBSnapshotIdentifier=final_snapshot_id
            )

        return {
            'statusCode': 200,
            'body': f"Deletion of RDS instance '{db_instance_id}' initiated.",
            'response': response
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

