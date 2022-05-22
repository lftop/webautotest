import win32com.client


def speak():
    speaker = win32com.client.Dispatch('SAPI.SPVOICE')
    speaker.Speak('Qing shu ru yan zheng ma')
