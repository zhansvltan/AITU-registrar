# Generated by Django 4.0.6 on 2022-07-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_alter_subjectlinkprofessor_professor_fk_and_more'),
        ('students', '0002_alter_student_group_fk'),
        ('professors', '0004_alter_professorlinkposition_position_fk_and_more'),
        ('groups', '0004_alter_grouplinkprofessorsubject_group_fk_and_more'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='group_1to1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='report',
            name='professor_1to1',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='professors.professor', verbose_name='Professor of Student Reported'),
        ),
        migrations.AddField(
            model_name='report',
            name='skipped_days',
            field=models.CharField(default='dd.mm.yyyy - dd.mm.yyyy', max_length=120, verbose_name='Days missed by student'),
        ),
        migrations.AddField(
            model_name='report',
            name='subject_1to1',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject', verbose_name='Subject of Student Reported'),
        ),
        migrations.AlterField(
            model_name='report',
            name='document_pdf',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Electronic Version of Document'),
        ),
        migrations.AlterField(
            model_name='report',
            name='student_1to1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.student', verbose_name='Student Reported'),
        ),
    ]