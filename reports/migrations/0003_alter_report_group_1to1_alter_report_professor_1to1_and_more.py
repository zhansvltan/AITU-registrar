# Generated by Django 4.0.6 on 2022-07-15 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_alter_subjectlinkprofessor_professor_fk_and_more'),
        ('groups', '0004_alter_grouplinkprofessorsubject_group_fk_and_more'),
        ('students', '0002_alter_student_group_fk'),
        ('professors', '0004_alter_professorlinkposition_position_fk_and_more'),
        ('reports', '0002_report_group_1to1_report_professor_1to1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='group_1to1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='report',
            name='professor_1to1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='professors.professor', verbose_name='Professor of Student Reported'),
        ),
        migrations.AlterField(
            model_name='report',
            name='student_1to1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.student', verbose_name='Student Reported'),
        ),
        migrations.AlterField(
            model_name='report',
            name='subject_1to1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject', verbose_name='Subject of Student Reported'),
        ),
    ]
