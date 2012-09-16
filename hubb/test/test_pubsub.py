from twisted.internet import defer

from urllib import urlencode

from hubb import test
from hubb.test import mocks

class TestPubSub(test.SiteTestCase):
    def setUp(self):
        super(TestPubSub, self).setUp()
        self.site.resource.putChild('mock_publisher', mocks.MockPublisher())
        self.site.resource.putChild('mock_subscriber', mocks.MockSubscriber())
        
    @defer.inlineCallbacks
    def testPublisherMock(self):
        resp = yield self.doRequest('/mock_publisher/happycats.xml')
        self.assertEqual('application/atom+xml', resp.info().dict['content-type'])
        
    @defer.inlineCallbacks
    def testSubscriberMock(self):
        challenge = '123'
        resp = yield self.doRequest('/mock_subscriber/callback?%s' % urlencode({'hub.challenge': challenge}))
        self.assertEqual(challenge, resp.read())

        
