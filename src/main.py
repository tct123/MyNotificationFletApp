import flet as ft
from mynotification import Notification
import flet_permission_handler as fph
import time


def main(page: ft.Page):
    ph = fph.PermissionHandler()
    page.overlay.append(ph)

    def request_permission():
        # Warte kurz, um sicherzustellen, dass die Seite vollständig geladen ist
        time.sleep(1)
        try:
            ph.request_permission(of=fph.PermissionType.NOTIFICATION)
        except:
            pass

    def on_notify_click(e):
        x = Notification(
            title="Hallo!",
            message="Dies ist eine Benachrichtigung über Pyjnius.",
            platform=page.platform.name,
        )
        x.send_mynotification()

    # Füge die Benutzeroberfläche hinzu
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    button = ft.ElevatedButton(
        text="Show Notification",
        on_click=on_notify_click,
        data=fph.PermissionType.NOTIFICATION,
    )
    page.add(
        ft.SafeArea(
            ft.Row(
                [button],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    )

    # Aktualisiere die Seite und starte die Berechtigungsanfrage
    page.update()
    request_permission()


ft.app(main)
