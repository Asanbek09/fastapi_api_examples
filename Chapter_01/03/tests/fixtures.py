import pytest

from models.events import EventUpdate

# Fixture is defined
@pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title = "FastAPI book launch",
        image = "https://examples.com/fastapi.png",
        description = "We will be discussing ...",
        tags = ["python", "fastapi", "book", "lauch"],
        location = "Google Meet"
    )

def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Book launch"