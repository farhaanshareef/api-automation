import pytest

# Import test classes from individual test files
from test.post_user import TestCreateUser
from test.update_user import TestUpdateUser
from test.patch_user import TestPatchUser
from test.delete_user import TestDeleteUser
from test.get_users import TestGetUser

class TestSmokeSuite:
    def test_run_smoke_suite(self):
        # Create instances of the test classes
        create_user_tests = TestCreateUser()
        update_user_tests = TestUpdateUser()
        patch_user_tests = TestPatchUser()
        delete_user_tests = TestDeleteUser()
        get_user_tests = TestGetUser()

        # Call test functions one by one
        print("Running Create User Test...")
        create_user_tests.test_create_user()

        print("Running Update User Test...")
        update_user_tests.test_put_user()

        print("Running Patch User Test...")
        patch_user_tests.test_patch_user()

        print("Running Delete User Test...")
        delete_user_tests.test_delete_user()

        print("Running Get User Test...")
        get_user_tests.test_get_users()
