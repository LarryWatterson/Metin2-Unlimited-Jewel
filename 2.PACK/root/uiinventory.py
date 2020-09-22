# find (in class inventorywindow (def _loadwindow)

		tooltip = uiToolTip.ToolTip()
		self.toolTip = tooltip

# add under
		self.tasonay = None

# find

		self.interface = None

# add under

		self.tasonay = None


# find

		elif item.IsKey(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

# add under

		elif int(srcItemVID) == 90028: #item vnum
			self.UnlimitedJewel(srcItemVID,srcItemSlotPos,dstItemSlotPos)

# find

		elif item.IsKey(srcItemVNum):
			return True

# add under

		elif int(srcItemVNum) == 90028: #item vnum
			return True

# find

		elif item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return True

# add under

		elif srcItemVNum == 90028:
			if self.__CanUseForArmor(srcItemVNum,srcSlotPos,dstSlotPos) == True:
				return True


# find

			elif "USE_COSTUME_ENCHANT" == useType:
				if self.__CanChangeCostumeAttrList(dstSlotPos):
					return True
			elif "USE_COSTUME_TRANSFORM" == useType:
				if self.__CanResetCostumeAttr(dstSlotPos):
					return True

		return False

# add under

	def __CanUseForArmor(self, srcitem, srcpos, dstSlotPos):
		dstItemVNum = playermeto.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False
		item.SelectItem(dstItemVNum)
		itemType = item.GetItemType()

		if itemType != item.ITEM_TYPE_BELT and not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):

#		if not item.GetItemType() == ITEM_TYPE_BELT or  item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		return True


	def UnlimitedJewel(self, srcitem, metinSlotPos, targetSlotPos):
		targetIndex = playermeto.GetItemIndex(targetSlotPos)
		item.SelectItem(targetIndex)
		itemName = item.GetItemName()
		itemType = item.GetItemType()

		if itemType != item.ITEM_TYPE_BELT and not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):

		#if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			chat.AppendChat(chat.CHAT_TYPE_INFO, translate.justtypearmor)
			return
			
		if targetIndex == 90028:
			return
		tasonay = uicommon.QuestionDialog2()
		tasonay.SetText1(translate.ischeckarmor %(str(itemName)))
		tasonay.SetText2(translate.ischeckarmor2)
		tasonay.SetAcceptEvent(lambda arg=True: self.checkOkey(arg, metinSlotPos, targetSlotPos))
		tasonay.SetCancelEvent(lambda arg=False: self.checkOkey(arg, metinSlotPos, targetSlotPos))
		tasonay.Open()
		self.tasonay = tasonay

	def checkOkey(self, onay, matkap, item):
		if self.tasonay:
			if onay:
				self.tasonay.Close()
				self.tasonay = None
				net.SendItemUseToItemPacket(matkap, item)
			else:
				self.tasonay.Close()
				self.tasonay = None