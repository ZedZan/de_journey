from unittest.mock import patch, MagicMock
from week5.cloud_sink import CloudSink
import pytest

def test_upload_called_with_correct_args():
    with patch("week5.cloud_sink.storage.Client") as mock_storage:
        with patch("week5.cloud_sink.bigquery.Client") as mock_bq:

            mock_storage_client = MagicMock()
            mock_bq_client = MagicMock()

            mock_storage.return_value = mock_storage_client
            mock_bq.return_value = mock_bq_client

            sink = CloudSink("bucket", "project", "dataset", "table")
            sink.export_to_cloud("week5/data/sales_dummy.csv")

            mock_storage_client.bucket.assert_called_once_with("bucket")
    

def test_bq_load_called():
    with patch("week5.cloud_sink.storage.Client") as mock_storage:
        with patch("week5.cloud_sink.bigquery.Client") as mock_bq:

            mock_storage_client = MagicMock()
            mock_bq_client = MagicMock()

            mock_storage.return_value = mock_storage_client
            mock_bq.return_value = mock_bq_client

            sink = CloudSink("bucket", "project", "dataset", "table")
            sink.export_to_cloud("week5/data/sales_dummy.csv")

            mock_bq_client.load_table_from_uri.assert_called_once()


def test_export_fails_on_upload_error():
    with patch("week5.cloud_sink.storage.Client") as mock_storage:
        mock_client = MagicMock()
        mock_storage.return_value = mock_client

        # Force GCS upload to fail BEFORE calling export_to_cloud
        mock_client.bucket.side_effect = Exception("GCS error")

        sink = CloudSink("bucket", "project", "dataset", "table")

        with pytest.raises(Exception, match="GCS error"):
            sink.export_to_cloud("week5/data/sales_dummy.csv")