import unittest
import server

class Test_test_addresses(unittest.TestCase):
    def test_inbox_root_url(self):
        inbox_url = server.get_inbox_root()
        self.assertEqual(inbox_url, "http://www.3gpp.org/ftp/Meetings_3GPP_SYNC/SA2/")
    def test_inbox_url(self):
        inbox_url = server.get_inbox_url()
        self.assertEqual(inbox_url, "http://www.3gpp.org/ftp/Meetings_3GPP_SYNC/SA2/Inbox/")
    def test_meeting_url(self):
        inbox_url = server.get_remote_meeting_folder('TSGS2_129BIS_West_Palm_Beach')
        self.assertEqual(inbox_url, "http://www.3gpp.org/ftp/tsg_sa/WG2_Arch/TSGS2_129BIS_West_Palm_Beach/")

if __name__ == '__main__':
    unittest.main()
