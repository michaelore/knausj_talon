from talon import Context, actions, ui, Module, app, clip
from typing import List, Union

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()
mod.apps.vscode = "app.name: emacs"

ctx.matches = r"""
app:  emacs
"""


@ctx.action_class("win")
class win_actions:
    def filename():
        title = actions.win.title()
        # title for shell: '*shell* - Doom Emacs'
        # TODO: support terminal tag

        if is_mac:# TODO: verify if needed
            result = title.split(" — ")[0]
        else:
            result = title.split(" - ")[0]

        if "." in result:
            return result

        return ""

    def file_ext():
        return actions.win.filename().split(".")[-1]
