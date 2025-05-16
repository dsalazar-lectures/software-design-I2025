from tests_example.app.blender_artifact import BlenderArtifact
from tests_example.app.attachments.blender_attachment import BlenderAttachment
from tests_example.app.attachments.mixer_attachment import MixerAttachment
from tests_example.app.attachments.processor_attachment import ProcessorAttachment
from tests_example.app.models.recipe import Recipe

def test_blender_attachment_normal_use():
    blender = BlenderArtifact(BlenderAttachment())
    result = blender.cook(3)
    assert result == "Blended for 3 min"
    assert blender.get_cooking_state() == "smooth"

def test_mixer_attachment_under_mixed():
    mixer = BlenderArtifact(MixerAttachment())
    result = mixer.cook(2)
    assert result == "Mixed for 2 min"
    assert mixer.get_cooking_state() == "under mixed"

def test_processor_attachment_over_processed():
    processor = BlenderArtifact(ProcessorAttachment())
    result = processor.cook(10)
    assert result == "Processed for 10 min"
    assert processor.get_cooking_state() == "mush"

def test_blender_artifact_with_recipe():
    blender = BlenderArtifact(BlenderAttachment())
    recipe = Recipe([blender])

    results = recipe.cook_all(3)
    states = recipe.get_all_states()

    assert results == ["Blended for 3 min"]
    assert states == ["smooth"]