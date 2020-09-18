@@ -90,7 +90,7 @@ def get_data(self):

	def send(self):

		eccoin.sendpacket(self.packet['_to'], self.packet['_id'], self.packet['_ver'], json.dumps(self.packet))
		eccoin.sendpacket(self.packet['_to'], self.packet['_id'], json.dumps(self.packet))

################################################################################

@@ -163,15 +163,25 @@ def main():
		print('*******************************************')
		print('')

		while True:
		bExit = False

		while not bExit:

			socks = dict(poller.poll())

			if sys.stdin.fileno() in socks:

				line = command_line_args.name + '> ' + sys.stdin.readline().strip('\n')
				line = sys.stdin.readline().strip('\n')

				if line == "exit":

					bExit = True

					continue

				ecc_packet = eccPacket(settings.protocol_id, settings.protocol_ver, command_line_args.tag, routingTag, eccPacket.TYPE_chatMsg, line)
				data = command_line_args.name + '> ' + line

				ecc_packet = eccPacket(settings.protocol_id, settings.protocol_ver, command_line_args.tag, routingTag, eccPacket.TYPE_chatMsg, data)

				ecc_packet.send()

@@ -211,6 +221,12 @@ def main():

							pass

	bufferCmd = 'ReleaseBufferRequest'

	bufferSig = eccoin.buffersignmessage(bufferKey, bufferCmd)

	eccoin.releasebuffer(settings.protocol_id, bufferSig)

	subscriber.close()
	context.term()
