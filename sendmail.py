#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2019 Red Hat, Inc.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/

"""Send e-mail report, used to send reports to our mailing list."""

from datetime import date
from email.mime.text import MIMEText
import os
import smtplib

_BEHAVE_REPORT_FILE = "behave-report.html"
_DEPLOYMENT_NAME = os.getenv("THOTH_DEPLOYMENT_NAME", "N/A")
_EMAIL_SMTP_SERVER = os.getenv("THOTH_EMAIL_SMTP_SERVER", "smtp.corp.redhat.com")
_EMAIL_TO = os.getenv("THOTH_EMAIL_TO", "aicoe-thoth@redhat.com")
_EMAIL_FROM = os.getenv("THOTH_EMAIL_FROM", "noreply@redhat.com")


def _create_email_subject() -> str:
    """Create e-mail subject."""
    today = date.today()
    return f"Integration tests update for {_DEPLOYMENT_NAME} ({today.strftime('%Y-%m-%d')})"


def send_email() -> None:
    """Send e-mail with begave test reports."""
    with open(_BEHAVE_REPORT_FILE, "r") as fp:
        msg = MIMEText(fp.read(), "html")

    msg["Subject"] = _create_email_subject()
    msg["From"] = _EMAIL_FROM
    msg["To"] = _EMAIL_TO

    s = smtplib.SMTP(_EMAIL_SMTP_SERVER)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string())
    s.quit()


__name__ == "__main__" and send_email()
