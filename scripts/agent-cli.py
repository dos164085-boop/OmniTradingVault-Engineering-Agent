#!/usr/bin/env python3

import argparse
import json
import sys

from datetime import datetime
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.repository import Repository
from src.core.incidents import IncidentRepository
from src.core.incident import Incident
from src.core.learning import LearningEngine
from src.core.search import SearchEngine
from src.core.incident_creator import IncidentCreator


class AgentCLI:

    def __init__(self):

        self.repo = Repository()
        self.version = self.repo.load_version()

        self.incidents = IncidentRepository()
        self.incident = Incident()

        self.learning = LearningEngine()
        self.search = SearchEngine()
        self.creator = IncidentCreator()

    def status(self):

        print(
            json.dumps(
                {
                    "agent": "Leo",
                    "status": "online",
                    "repository": self.repo.root.name,
                    "version": self.version.get("agent_version"),
                    "trust_level": self.version.get("trust_level"),
                    "knowledge": "available",
                    "runtime": "available",
                    "timestamp": datetime.now().isoformat(),
                },
                indent=2,
            )
        )

    def version_command(self):

        print(
            json.dumps(
                self.version,
                indent=2,
            )
        )

    def projects(self):

        print(
            json.dumps(
                {
                    "projects": self.repo.list_projects()
                },
                indent=2,
            )
        )

    def incidents_command(self):

        incidents = self.incidents.list()

        print(
            json.dumps(
                {
                    "total": len(incidents),
                    "incidents": incidents,
                },
                indent=2,
            )
        )

    def incident_command(self, incident_id):

        incident = self.incident.load(incident_id)

        print("=" * 70)
        print(f"INCIDENTE: {incident['incident']['id']}")
        print("=" * 70)
        print()

        print(f"Proyecto  : {incident['incident']['project']}")
        print(f"Estado    : {incident['incident']['status']}")
        print(f"Prioridad : {incident['incident']['priority']}")
        print(f"Severidad : {incident['incident']['severity']}")
        print()

        print("Título")
        print("-" * 70)
        print(incident["incident"]["title"])
        print()

        print("Resumen")
        print("-" * 70)
        print(incident["summary"])
        print()

        print("Cronología")
        print("-" * 70)
        print(incident["timeline"])
        print()

        print("Lecciones Aprendidas")
        print("-" * 70)
        print(incident["lessons"])
        print()

        print("=" * 70)

    def learn_command(self, incident_id):

        report = self.learning.learn(incident_id)

        print("=" * 70)
        print("LEARNING REPORT")
        print("=" * 70)
        print()

        print(f"Incident   : {report['incident']}")
        print(f"Project    : {report['project']}")
        print(f"Confidence : {report['confidence']}")
        print()

        print("Patterns")
        print("-" * 70)

        if report["patterns"]:

            for pattern in report["patterns"]:
                print(f"• {pattern}")

        else:

            print("No patterns registered.")

        print()

        print("Engineering Lessons")
        print("-" * 70)

        if report["lessons"]:

            for lesson in report["lessons"]:
                print(f"• {lesson}")

        else:

            print("No lessons available.")

        print()
        print("=" * 70)

    def search_command(self, query):

        results = self.search.search(query)

        print("=" * 70)
        print("RESULTADOS DE BÚSQUEDA")
        print("=" * 70)
        print()

        print(f"Consulta : {query}")
        print(f"Incidentes encontrados : {len(results)}")
        print()

        if not results:

            print("No se encontraron coincidencias.")
            print()
            print("=" * 70)
            return

        for incident in results:

            print("-" * 70)
            print(incident["id"])
            print("-" * 70)
            print()

            print(f"Título      : {incident['title']}")
            print(f"Proyecto    : {incident['project']}")
            print(f"Estado      : {incident['status']}")
            print(f"Confianza   : {incident['confidence']}")

            patterns = incident.get("patterns", [])

            if patterns:
                print(
                    f"Patrones    : {', '.join(patterns)}"
                )

            print()

        print("=" * 70)

    def create_incident_command(self, incident_id):

        path = self.creator.create(incident_id)

        print("=" * 70)
        print("NEW INCIDENT CREATED")
        print("=" * 70)
        print()

        print(f"Incident : {incident_id}")
        print(f"Location : {path}")
        print()

        print("Structure created")
        print("-" * 70)

        print("incident.yaml")
        print("summary.md")
        print("timeline.md")
        print("lessons-learned.md")
        print("decisions/")
        print("evidence/")
        print("hypotheses/")
        print("iterations/")

        print()
        print("=" * 70)

    def run(self):

        parser = argparse.ArgumentParser(
            description="Leo Engineering Platform"
        )

        parser.add_argument(
            "command",
            help="Command to execute"
        )

        parser.add_argument(
            "arguments",
            nargs="*",
            help="Command arguments"
        )

        args = parser.parse_args()

        if args.command == "incident":

            if len(args.arguments) != 1:

                print("Uso:")
                print(
                    "python scripts/agent-cli.py incident ENG-0001"
                )
                return

            self.incident_command(args.arguments[0])
            return

        if args.command == "learn":

            if len(args.arguments) != 1:

                print("Uso:")
                print(
                    "python scripts/agent-cli.py learn ENG-0001"
                )
                return

            self.learn_command(args.arguments[0])
            return

        if args.command == "search":

            if len(args.arguments) != 1:

                print("Uso:")
                print(
                    "python scripts/agent-cli.py search foundry"
                )
                return

            self.search_command(args.arguments[0])
            return

        if args.command == "create":

            if len(args.arguments) != 1:

                print("Uso:")
                print(
                    "python scripts/agent-cli.py create ENG-0002"
                )
                return

            self.create_incident_command(
                args.arguments[0]
            )
            return

        commands = {
            "status": self.status,
            "version": self.version_command,
            "projects": self.projects,
            "incidents": self.incidents_command,
        }

        command = commands.get(args.command)

        if command is None:

            print(
                f"Comando '{args.command}' no soportado."
            )
            print()
            print("Comandos disponibles:")
            print()

            print("  status")
            print("  version")
            print("  projects")
            print("  incidents")
            print("  incident <ID>")
            print("  learn <ID>")
            print("  search <texto>")
            print("  create <ID>")

            return

        command()


if __name__ == "__main__":
    AgentCLI().run()