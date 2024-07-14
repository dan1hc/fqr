const core = require("@actions/core");
const github = require("@actions/github");

const restClient = github.getOctokit(core.getInput('token'));

restClient.rest.pulls.listFiles(
    {
        owner: "dan1hc",
        repo: "fqr",
        per_page: 100,
        pull_number: github.context.payload.pull_request.number
        }
    ).then((response) => {
        if (response.data.length >= 100) {
            core.setFailed(
                "No more than 99 files may be changed per pull request."
            );
        } else {
            var semantic_release_tracker = 0;
            var pyfile_changed = false;
            response.data.forEach(record => {
                var filename = record.filename;
                console.log(`FILENAME: ${filename}`);
                console.log("");
                if (
                    filename.endsWith('pyproject.toml')
                    || filename.endsWith('fqr/__init__.py')
                    ) {
                        semantic_release_tracker += 1
                    } else if (filename.endsWith('.py')) {
                        pyfile_changed = true;
                    };
            });
            const is_semantic_release_required = (
                semantic_release_tracker === 2
            );
            const is_testing_required = (
                pyfile_changed === true
                && semantic_release_tracker < 2
            );
            core.setOutput(
                'is_semantic_release_required',
                is_semantic_release_required
            );
            console.log(`RELEASE REQUIRED: ${is_semantic_release_required}`);
            core.setOutput('is_testing_required', is_testing_required);
            console.log(`TESTING REQUIRED: ${is_testing_required}`);
        };
    }, (error) => {
        core.setFailed(error);
        }
    );
