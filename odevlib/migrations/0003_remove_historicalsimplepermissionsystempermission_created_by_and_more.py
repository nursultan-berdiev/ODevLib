# Generated by Django 4.2.2 on 2023-09-15 16:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("odevlib", "0002_added_request_logger"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalsimplepermissionsystempermission",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="historicalsimplepermissionsystempermission",
            name="history_user",
        ),
        migrations.RemoveField(
            model_name="historicalsimplepermissionsystempermission",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="requestlogentry",
            name="user",
        ),
        migrations.AlterUniqueTogether(
            name="simplepermissionassignment",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="simplepermissionassignment",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="simplepermissionassignment",
            name="permission",
        ),
        migrations.RemoveField(
            model_name="simplepermissionassignment",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="simplepermissionassignment",
            name="user",
        ),
        migrations.RemoveField(
            model_name="simplepermissionsystempermission",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="simplepermissionsystempermission",
            name="updated_by",
        ),
        migrations.DeleteModel(
            name="HistoricalSimplePermissionAssignment",
        ),
        migrations.DeleteModel(
            name="HistoricalSimplePermissionSystemPermission",
        ),
        migrations.DeleteModel(
            name="RequestLogEntry",
        ),
        migrations.DeleteModel(
            name="SimplePermissionAssignment",
        ),
        migrations.DeleteModel(
            name="SimplePermissionSystemPermission",
        ),
    ]
