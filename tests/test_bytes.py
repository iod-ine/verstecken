import shutil
import pathlib
import tempfile

import verstecken


def test_reverse_file():
    """Test the file reversing function."""

    payload = "kaggle-pipeline-main.zip"

    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copy(pathlib.Path("payloads") / payload, tmpdir)
        payload = pathlib.Path(tmpdir) / "kaggle-pipeline-main.zip"
        daolyap = pathlib.Path(tmpdir) / "piz.niam-enilepip-elggak.dat"
        verstecken.reverse_file(payload)

        assert daolyap.exists()

        with open(payload, "br") as o:
            original = o.read()

        with open(daolyap, "br") as r:
            reversed_ = r.read()

        assert original == reversed_[::-1]

        payload.unlink()
        verstecken.reverse_file(daolyap)

        assert payload.exists()

        with open(payload, "br") as o:
            original = o.read()

        assert original == reversed_[::-1]
