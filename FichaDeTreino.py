import tkinter as tk
import random

def atualizar_lista():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    peso = float(entry_peso.get())
    lista_exercicios = []
    if idade < 30:
        lista_exercicios = [
            "Segunda-feira - Membros Superiores:",
            "Supino reto (4x10) - Descanso: 1 minuto",
            "Rosca direta (3x12) - Descanso: 45 segundos",
            "Supino fechado (4x10) - Descanso: 1 minuto",
            "Tríceps francês (3x12) - Descanso: 45 segundos",
            "",
            "Terça-feira - Membros Inferiores:",
            "Agachamento (4x10) - Descanso: 1 minuto",
            "Leg press 45° (3x12) - Descanso: 45 segundos",
            "Cadeira extensora (3x12) - Descanso: 45 segundos",
            "Banco romano (4x10) - Descanso: 1 minuto",
            "",
            "Quarta-feira - Membros Superiores:",
            "Desenvolvimento de ombros (4x10) - Descanso: 1 minuto",
            "Tríceps pulley (3x12) - Descanso: 45 segundos",
            "Rosca Martelo (3x12) - Descanso: 45 segundos",
            "",
            "Quinta-feira - Membros Inferiores:",
            "Cadeira extensora (3x12) - Descanso: 45 segundos",
            "Flexora deitado (3x12) - Descanso: 45 segundos",
            "",
            "Sexta-feira - Abdômen:",
            "Prancha (3x30 segundos) - Descanso: 30 segundos",
            "Crunch",
            ""
        ]
    else:
        lista_exercicios = [
            "Segunda-feira - Membros Superiores:",
            "Supino inclinado (4x10) - Descanso: 1 minuto",
            "Rosca alternada (3x12) - Descanso: 45 segundos",
            "",
            "Terça-feira - Membros Inferiores:",
            "Agachamento livre (4x10) - Descanso: 1 minuto",
            "Cadeira extensora (3x12) - Descanso: 45 segundos",
            "Elevação de glúteo (3x12) - Descanso: 45 segundos",
            "",
            "Quarta-feira - Membros Superiores:",
            "Desenvolvimento militar (4x10) - Descanso: 1 minuto",
            "Tríceps francês (3x12) - Descanso: 45 segundos",
            "Elevação frontal (3x12) - Descanso: 45 segundos",
            "Elevação lateral (3x12) - Descanso: 45 segundos",
            "Desenvolvimento (3x12) - Descanso: 1 minuto",
            "",
            "Quinta-feira - Membros Inferiores:",
            "Leg press 45° (3x12) - Descanso: 45 segundos",
            "Stiff (3x12) - Descanso: 45 segundos",
            "Agachamento livre (3x12) - Descanso: 45 segundos",
            "Levantamento terra romeno",
            "",
            "Sexta-feira - Abdômen:",
            "Prancha lateral (3x30 segundos) - Descanso: 30 segundos",
            "Elevação de pernas suspenso",
            "Abdominal supra",
            "Abdominal infra"
        ]