from src.core.indexer import KnowledgeIndexer


class KnowledgeValidator:

    REQUIRED_FIELDS = [
        "id",
        "title",
        "project",
        "status",
        "confidence",
    ]

    def __init__(self):

        self.indexer = KnowledgeIndexer()

    def validate(self):

        report = []

        for incident in self.indexer.incidents():

            metadata = incident["incident"]

            missing = []

            for field in self.REQUIRED_FIELDS:

                value = metadata.get(field)

                if value in (None, "", []):
                    missing.append(field)

            report.append(
                {
                    "id": metadata.get("id", "UNKNOWN"),
                    "valid": len(missing) == 0,
                    "missing": missing,
                }
            )

        return report

    def summary(self):

        validation = self.validate()

        valid = 0
        invalid = 0

        for item in validation:

            if item["valid"]:
                valid += 1
            else:
                invalid += 1

        return {
            "total": len(validation),
            "valid": valid,
            "invalid": invalid,
            "details": validation,
        }
    