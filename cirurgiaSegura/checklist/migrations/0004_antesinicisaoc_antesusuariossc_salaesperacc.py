# Generated by Django 4.1 on 2022-10-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checklist", "0003_pacientecirurgia_delete_dadosusuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="AntesInicisaoC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("todosProfissionaisCNF", models.CharField(max_length=1)),
                ("cirurgiaoAnestesistaEEC", models.CharField(max_length=15)),
                ("antibioticoProfilaticoAU", models.CharField(max_length=1)),
                ("horaAPAU", models.TimeField()),
                ("examesImagemD", models.CharField(max_length=1)),
                ("RevisaoCirurgiaoECDP", models.CharField(max_length=1)),
                ("qualRCECDP", models.CharField(max_length=15)),
                ("RevisaoAnestesistaAPERU", models.CharField(max_length=1)),
                ("RevisaoEnfermagemICEC", models.CharField(max_length=1)),
                ("palcaBisturiP", models.CharField(max_length=1)),
                ("EquipamentoTestadoF", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="AntesUsuarioSSC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instrumentaisAntes", models.IntegerField()),
                ("compressasAntes", models.IntegerField()),
                ("agulhasAntes", models.IntegerField()),
                ("laminaBisturiAntes", models.IntegerField()),
                ("instrumentaisDepois", models.IntegerField()),
                ("compressasDepois", models.IntegerField()),
                ("agulhasDepois", models.IntegerField()),
                ("laminaBisturiDepois", models.IntegerField()),
                ("RegistoCompletoPIRLP", models.CharField(max_length=1)),
                ("houveAglumPMEI", models.CharField(max_length=1)),
                ("QualHAPMEI", models.CharField(max_length=1)),
                ("altaConfirmadaAE", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="SalaEsperaCC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pulseriaIdentificacao", models.CharField(max_length=1)),
                ("jejum", models.CharField(max_length=1)),
                ("inicioJ", models.TimeField()),
                ("triconomiaRealizada", models.CharField(max_length=1)),
                ("realizouBanho", models.CharField(max_length=1)),
                ("preparoIntestinal", models.CharField(max_length=1)),
                ("semProtese", models.CharField(max_length=1)),
                ("sitioCirurgico", models.CharField(max_length=1)),
                ("alergiasConhecidas", models.CharField(max_length=1)),
                ("QualAC", models.CharField(max_length=20)),
                ("riscoViaA", models.CharField(max_length=1)),
                ("EquipamentoDisponivelRVA", models.IntegerField()),
                ("riscoPerdaSa", models.CharField(max_length=1)),
                ("equipamentosAnestesiaTF", models.CharField(max_length=15)),
                ("CaixasInstrumentaisCPE", models.CharField(max_length=1)),
                ("formularioIdentificacao", models.CharField(max_length=1)),
                ("relatorioEnfermagem", models.CharField(max_length=1)),
                ("fichaSinaisV", models.CharField(max_length=1)),
                ("exameLaboratI", models.CharField(max_length=1)),
                ("consentimentoCirurgico", models.CharField(max_length=1)),
                ("consentimentoAnestésico", models.CharField(max_length=1)),
                ("avaliaçãoPreA", models.CharField(max_length=1)),
            ],
        ),
    ]
