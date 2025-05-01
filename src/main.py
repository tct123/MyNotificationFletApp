import flet as ft
from mynotification import Notification
import flet_permission_handler as fph
import time


def main(page: ft.Page):
    # Initialisiere den Permission Handler
    try:
        ph = fph.PermissionHandler()
        page.overlay.append(ph)
    except Exception as e:
        print(f"Fehler beim Initialisieren des Permission Handlers: {e}")
        return

    # Funktion zum Anfordern von Berechtigungen
    def request_permission():
        # Warte kurz, um sicherzustellen, dass die Seite vollständig geladen ist
        time.sleep(1)
        try:
            ph.request_permission(of=fph.PermissionType.NOTIFICATION)
            print("Berechtigung erfolgreich angefordert.")
        except Exception as e:
            print(f"Fehler bei der Berechtigungsanforderung: {e}")

    # Funktion zum Senden einer Benachrichtigung
    def on_notify_click(e):
        try:
            x = Notification(
                title="Hallo!",
                message="Dies ist eine Benachrichtigung über Pyjnius.",
                platform=page.platform.name,
            )
            x.send_mynotification()
            print("Benachrichtigung erfolgreich gesendet.")
        except Exception as e:
            print(f"Fehler beim Senden der Benachrichtigung: {e}")

    # Benutzeroberfläche erstellen
    try:
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
        page.update()
        print("Benutzeroberfläche erfolgreich geladen.")
    except Exception as e:
        print(f"Fehler beim Erstellen der Benutzeroberfläche: {e}")
        return

    # Berechtigungen anfordern
    request_permission()


# Hauptprogramm starten
ft.app(main)
