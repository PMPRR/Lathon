from lathon.environment import Environment


class Tabular(Environment):

    def __init__(self, columns_spec: str = None):

        columns_spec = columns_spec.replace(" ", "")
        ALL_POSSIBLE_COL_SPECS = ("|", "r", "l", "c")
        for spec in columns_spec:
            if spec not in ALL_POSSIBLE_COL_SPECS:
                raise AssertionError(f"specification character {spec} not allowed")

        shortened_column_spec = columns_spec.replace(" ", "")
        shortened_column_spec = shortened_column_spec.replace("|", "")
        self.lenght = len(shortened_column_spec)

        super().__init__(name="tabular", optional_arguments=columns_spec)
        self.rows: list[list] = None
        return

    def addRow(self, row: list):
        """
        Parameter
        ---------
        row: list
        A list of elements to be added to the table
        """

        if self.rows is None:
            self.rows = [row]
            return

        if len(self.rows[0]) != self.lenght:
            raise AssertionError(
                f"The row could not be added, expected {len(self.rows)}, received {len(row)}"
            )

        self.rows.append(row)
        return

    def _dumps_text(self):
        text = ""

        for row in self.rows:
            text += "\n"
            row_str = [str(r) for r in row]
            text += " & ".join(row_str)
            text += r" \\"

        return text
