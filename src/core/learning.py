from src.core.incident import Incident


class LearningEngine:

    def __init__(self):
        self.incident = Incident()

    def learn(self, incident_id):

        data = self.incident.load(incident_id)

        report = {
            "incident": data["incident"]["id"],
            "project": data["incident"]["project"],
            "patterns": data["incident"].get("patterns", []),
            "confidence": data["incident"].get("confidence", "Unknown"),
            "lessons": self._extract_lessons(
                data.get("lessons", "")
            )
        }

        return report

    def _extract_lessons(self, text):

        lessons = []
        paragraph = []

        for raw_line in text.splitlines():

            line = raw_line.strip()

            if not line:

                if paragraph:

                    lessons.append(
                        " ".join(paragraph)
                    )

                    paragraph = []

                continue

            if line.startswith("#"):

                if paragraph:

                    lessons.append(
                        " ".join(paragraph)
                    )

                    paragraph = []

                continue

            if line.startswith("-"):

                if paragraph:

                    lessons.append(
                        " ".join(paragraph)
                    )

                    paragraph = []

                lessons.append(
                    line[1:].strip()
                )

                continue

            paragraph.append(line)

        if paragraph:

            lessons.append(
                " ".join(paragraph)
            )

        return lessons