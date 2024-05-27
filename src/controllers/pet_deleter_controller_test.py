from src.controllers.pet_deleter_controller import PetDeleterController


def test_delete_pet(mocker) -> None:
    mock_repository = mocker.Mock()

    controller = PetDeleterController(pets_repository=mock_repository)
    controller.delete_pet(name="petName")

    mock_repository.delete_pets.assert_called_once_with(name="petName")
