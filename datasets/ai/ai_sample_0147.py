#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
BPMN diagram for FOMDES process 1
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bpmn_pgv import *
import pygraphviz as pgv

__author__ = 'mapologo'

PROCESS_LABEL = "Liquidación de Créditos"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

se_cluster = {"se7": ("Recibir el documento protocolizado", "start"),
              "se8": ("Revisar el documento protocolizado", "human"),
              "se9": ("", "end")}

se_edges = {"se7": {"se8": {}},
            "se8": {"se9": {"style": "invis"}}}

SE = add_cluster(F, "se", "Secretaría Ejecutiva", se_cluster, se_edges)

p_cluster = {"p1": ("Firma del cheque", "human"),
             "p2": ("Entregar cheque a beneficiario", "message")}

p_edges = {"p1":{"p2": {}}}

P = add_cluster(F, "p", "Presidencia", p_cluster, p_edges)

pr_cluster = {"pr2": ("Verificar documentación legal y elaborar certificación de disponibilidad", "human"),
              "pr3": ("Crear las cuentas por cobrar", "human"),
              "pr4": ("Generar tablas de amortización", "human"),
              "pr5": ("Imprimir y firmar orden de liquidación y cheque", "human")}

pr_edges = {"pr2": {"pr3": {}},
            "pr3": {"pr4": {}},
            "pr4": {"pr5": {}}}

PR = add_cluster(F, "pr", "Presupuesto/Administración", pr_cluster, pr_edges)

F.add_node("SIGEFOMDES Administración", image=IMAGE_PATH + "database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Administración")
F.add_node("SISAC", image=IMAGE_PATH + "database.png", shape="plaintext", label="", xlabel="SISAC")

global_edges = {"Beneficiario":  {"se7": {"style": "dashed"}},
                "se8": {"pr2": {"style": "dashed"}},
                "pr3": {"SIGEFOMDES Administración": {"style": "dashed"}},
                "pr4": {"SISAC": {"style": "dashed"}},
                "pr5": {"p1": {"style": "dashed"}},
                "p2": {"se9": {"style": "dashed"}, "Beneficiario": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc4.png", prog='dot')
F.write("proc4.dot")