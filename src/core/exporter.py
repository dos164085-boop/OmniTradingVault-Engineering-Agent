import json
from pathlib import Path

from src.core.indexer import KnowledgeIndexer


class KnowledgeExporter:

    def __init__(self):

        self.indexer = KnowledgeIndexer()

    def export_json(self, output_path):

        incidents = self.indexer.incidents()

        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                incidents,
                file,
                indent=2,
                ensure_ascii=False,
            )

        return output

    def export_summary(self, output_path):

        incidents = self.indexer.incidents()

        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output.open(
            "w",
            encoding="utf-8",
        ) as file:

            file.write("# Leo Engineering Knowledge\n\n")

            file.write(
                f"Total incidents: {len(incidents)}\n\n"
            )

            for incident in incidents:

                metadata = incident["incident"]

                file.write(
                    f"## {metadata['id']} - {metadata['title']}\n"
                )

                file.write(
                    f"- Project: {metadata.get('project', '')}\n"
                )

                file.write(
                    f"- Status: {metadata.get('status', '')}\n"
                )

                file.write(
                    f"- Confidence: {metadata.get('confidence', '')}\n"
                )

                patterns = metadata.get("patterns", [])

                if patterns:

                    file.write(
                        f"- Patterns: {', '.join(patterns)}\n"
                    )

                file.write("\n")

        return output
    