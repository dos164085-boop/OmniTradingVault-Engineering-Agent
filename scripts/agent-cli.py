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


class AgentCLI:

    def __init__(self):

        self.repo = Repository()
        self.version = self.repo.load_version()
        self.incidents = IncidentRepository()
        self.incident = Incident()

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
                    "timestamp": datetime.now().isoformat()
                },
                indent=2
            )
        )

    def version_command(self):

        print(json.dumps(self.version, indent=2))

    def projects(self):

        print(
            json.dumps(
                {
                    "projects": self.repo.list_projects()
                },
                indent=2
            )
        )

    def incidents_command(self):

        incidents = self.incidents.list()

        print(
            json.dumps(
                {
                    "total": len(incidents),
                    "incidents": incidents
                },
                indent=2
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

    def run(self):

        parser = argparse.ArgumentParser(
            description="Leo Engineering Platform"
        )

        parser.add_argument("command")
        parser.add_argument("arguments", nargs="*")

        args = parser.parse_args()

        if args.command == "incident":

            if len(args.arguments) != 1:
                print("Uso:")
                print("python scripts/agent-cli.py incident ENG-0001")
                return

            self.incident_command(args.arguments[0])
            return

        commands = {
            "status": self.status,
            "version": self.version_command,
            "projects": self.projects,
            "incidents": self.incidents_command,
        }

        command = commands.get(args.command)

        if command is None:

            print(f"Comando '{args.command}' no soportado.")
            print()
            print("Comandos disponibles:")

            for cmd in sorted(commands.keys()):
                print(f"  {cmd}")

            print("  incident <ID>")
            return

        command()


if __name__ == "__main__":
    AgentCLI().run()