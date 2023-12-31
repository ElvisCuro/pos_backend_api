# Generated by Django 3.2 on 2023-09-02 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_plato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedido_fech', models.DateTimeField(auto_now_add=True)),
                ('pedido_nro', models.CharField(max_length=100)),
                ('pedido_est', models.CharField(choices=[('solicitado', 'SOLICITADO'), ('entregado', 'ENTREGADO')], default='solicitado', max_length=100)),
                ('mesa_id', models.ForeignKey(db_column='mesa_id', on_delete=django.db.models.deletion.RESTRICT, to='api.mesa')),
                ('usu_id', models.ForeignKey(db_column='usu_id', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='Pedidos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_pedido',
            },
        ),
        migrations.CreateModel(
            name='PedidoPlato',
            fields=[
                ('pedidoplato_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedidoplato_cant', models.IntegerField(default=1)),
                ('pedido_id', models.ForeignKey(db_column='pedido_id', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.pedido')),
                ('plato_id', models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidosplatos', to='api.plato')),
            ],
            options={
                'db_table': 'tbl_pedido_plato',
            },
        ),
    ]
