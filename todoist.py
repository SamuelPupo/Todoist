
from time import sleep

from uiautomator import Device


def main():
    # The device must be unlocked and connected
    device = Device('823Y00168')
    
    # Turn on screen
    device.screen.on()
    # Go to home screen
    device.press.home()
    
    # Close n recent apps
    close_all(device)

    install_app(device)

    # Device information
    #print(device.info)
    # Screen information as xml
    #print(device.dump())
    
    # The app must be on the home screen
    #device(text="Todoist").click()
    #device.wait.update()
    
    # Use email
    #email_login(device)
    
    # Use Google account
    google_login(device)
    
    # More options
    #more_options_login(device)


def close_all(device):
    device.press.recent()
    for _ in range(10):
        device.swipe(500, 500, 500, 0, steps=10)
        sleep(1)


def install_app(device):
    device(text="Play Store").click()
    # Waits till there is a screen update
    device.wait.update()
    sleep(3)
    
    # Search the app
    device(text="Search for apps & games").set_text('todoist')
    device.press.enter()
    device.wait.update()
    
    # Install the app
    device(description="Install").click()
    device.wait.update()
    
    # Open the app
    device(description="Open").click()
    device.wait.update()


def email_login(device):
    device(text="Continue with email").click()
    device.wait.update()
    
    # Select account
    device(text="Test").click()
    device.wait.update()
    
    # Enter password
    device(text="Password").set_text('1234')
    
    device(text="LOG IN").click()
    device.wait.update()


def google_login(device):
    device(text="Continue with Google").click()
    device.wait.update()

    # Select account
    device(text="Test").click()
    device.wait.update()
    

def more_options_login(device):
    device(text="Continue with more options").click()
    device.wait.update()
    
    # Use Facebook
    facebook_login(device)
    
    # Use Apple
    #apple_login(device)
    
    
def facebook_login(device):
    device(text="Continue with Facebook").click()
    device.wait.update()
    
    # Account email
    device(resourceId="m_login_email").set_text('test@gmail.com')
    
    # Account password
    device(resourceId="m_login_password").set_text('1234')
    
    device(text="Log in").click()
    device.wait.update()


def apple_login(device):
    device(text="Continue with Apple").click()
    device.wait.update()
    
    # Account email
    device(resourceId="account_name_text_field").set_text('test@gmail.com')
    
    device(text="Continue").click()
    device.wait.update()
    
    # Account password
    device(resourceId="password_text_field").set_text('1234')
    
    device(resourceId="sign-in").click()
    device.wait.update()


if __name__ == "__main__":
    main()
