class Environment:
    """
    \\begin{name}[optional_arguments]{mandatory_arguments}
        ...
    \\end{name}
    """

    def __init__(
        self,
        name: str,
        optional_arguments: str | None = None,
        mandatory_arguments: str | None = None,
    ):

        self._name: str = name
        self._optional_arguments: str | None = optional_arguments
        self._mandatory_arguments: str | None = mandatory_arguments
        return

    def _dumps_text(self):
        return ""

    def __str__(self):
        text = f"\\begin{{{self._name}}}"

        text = (
            text
            if self._optional_arguments is None
            else text + f"[{self._optional_arguments}]"
        )

        text = (
            text
            if self._mandatory_arguments is None
            else text + f"{{{self._mandatory_arguments}}}"
        )

        # Adds inside text whith a "\t"

        inside = self._dumps_text()

        inside = inside.split("\n")
        inside = ["\t" + line for line in inside]
        inside = "\n".join(inside)
        text += inside

        # Add the \end{name}1
        text += f"\n\\end{{{self._name}}}\n"
        return text
